import json
import re
import requests
import time
import threading
from datetime import datetime


class AcompanhaLegis():
    d = {
        'host': 'https://dadosabertos.camara.leg.br/api/v2',
        'summary': [],
        'temas': [],
        'tram': [],
    }

    def __init__(self, dep, ano):
        self.d.update({
            'ano': ano,
            'id': self.get_dep_id(
                dep
            ),
        })

    def get_dep_id(self, name):
        id = 0
        params = {
            'nome': name
        }

        res = requests.get(
            '{}/deputados'.format(
                self.d.get('host')
            ),
            params=params,
            stream=True
        ).json()

        if len(res.get('dados', [])) > 0:
            id = res['dados'][0]['id']

        return id

    def get_prop(self, dep_id):
        ids = []
        tipos = [
            'PL',
            'PDL',
            'PRC',
            'PEC',
        ]
        params = {
            'idDeputadoAutor': dep_id,
            'ano': self.d.get('ano'),
            'siglaTipo': '',
            'itens': 100
        }

        for sigla in tipos:
            params['siglaTipo'] = sigla

            res = requests.get(
                '{}/proposicoes'.format(
                    self.d.get('host'),
                ),
                params=params,
                stream=True
            ).json()

            if len(res.get('dados', [])) > 0:
                for prop in res['dados']:
                    ids.append(prop['id'])

        return ids

    def set_temas(self, id):
        d = {
            'id': id,
            'temas': [],
        }

        res = requests.get(
            '{}/proposicoes/{}/temas'.format(
                self.d.get('host'),
                id,
            ),
            stream=True
        ).json()

        if len(res.get('dados', [])) > 0:
            for data in res['dados']:
                d['temas'].append(
                    data['tema']
                )

        self.d['temas'].append(
            d
        )

    def set_tram(self, id):
        d = {
            'id': id,
            'relator': '',
            'ultima_movimentacao': [],
        }

        res = requests.get(
            '{}/proposicoes/{}/tramitacoes'.format(
                self.d.get('host'),
                id,
            ),
            stream=True
        ).json()

        if len(res.get('dados', [])) > 0:
            res['dados'].reverse()

            for i in range(len(res['dados'])):
                tram = res.get('dados')[i]
                cod = str(tram.get('codTipoTramitacao'))
                despacho = re.sub(
                    r'regime de tramitação.+',
                    '',
                    tram.get('despacho'),
                    flags=re.IGNORECASE
                )

                if tram.get('siglaOrgao').upper() == 'MESA':
                    found = re.findall(
                        r'proposição sujeita à apreciação.+',
                        despacho,
                        flags=re.IGNORECASE
                    )
                    if found:
                        d['apreciacao'] = found[0].strip()

                    found = re.findall(
                        r'à[s]? comiss.+',
                        despacho,
                        flags=re.IGNORECASE
                    )
                    if found:
                        d['comissao_destinado'] = found[0].strip()

                if cod == '100':
                    d['tramitacao'] = tram.get('regime')
                elif cod == '129':
                    found = re.findall(
                        r'apense-se.+',
                        despacho,
                        flags=re.IGNORECASE
                    )
                    if found:
                        d['apensado'] = found[0].strip()
                elif cod == '320':
                    d['relator'] = despacho

                if i < 3:
                    d['ultima_movimentacao'].append(
                        '{} - {}'.format(
                            datetime.strptime(
                                tram.get('dataHora'),
                                '%Y-%m-%dT%H:%M'
                            ).strftime('%d/%m/%y às %H:%M'),
                            despacho,
                        )
                    )

        self.d['tram'].append(
            d
        )

    def set_summary(self, id):
        d = {
            'id': id,
            'comissao_atual': '',
            'comissao_destinado': '',
        }

        res = requests.get(
            '{}/proposicoes/{}'.format(
                self.d.get('host'),
                id,
            ),
            stream=True
        ).json()

        prop = res.get('dados')

        d['ano'] = int(prop.get('ano'))
        d['proposicao'] = prop.get('siglaTipo').upper()
        d['numero'] = int(prop.get('numero'))
        d['apresentacao'] = datetime.strptime(
            prop.get('dataApresentacao'),
            '%Y-%m-%dT%H:%M'
        ).strftime('%d/%m às %H:%M')
        d['ementa'] = prop.get('ementa')
        d['link'] = prop.get('uri')

        self.d['summary'].append(
            d
        )

    def do_data(self, dep_id):
        a = []
        b = []
        c = []
        res = []
        count = 0

        props = self.get_prop(
            dep_id
        )

        for id in props:
            summary = threading.Thread(
                target=self.set_summary,
                args=(
                    id,
                )
            )

            temas = threading.Thread(
                target=self.set_temas,
                args=(
                    id,
                )
            )

            tram = threading.Thread(
                target=self.set_tram,
                args=(
                    id,
                )
            )

            a.append(summary)
            b.append(tram)
            c.append(temas)

        for i in range(len(props)):
            print(
                '{0:.0%} '.format(
                    count/len(props)
                ),
                end='',
                flush=True
            )

            if i > 0:
                a[i-1].join()
            a[i].start()

            if i > 0:
                b[i-1].join()
            b[i].start()

            if i > 0:
                c[i-1].join()
            c[i].start()

            count += 1

        for i in range(len(props)):
            a[i].join()
            b[i].join()
            c[i].join()

        for i in range(len(props)):
            res.append({
                **self.d['summary'][i],
                **self.d['tram'][i],
                **self.d['temas'][i],
            })

        return res

    def main(self):
        start_time = time.time()
        print(
            '\nColetando dados...'
        )

        result = self.do_data(
            self.d.get('id')
        )

        print(
            str(
            '\n\nDados coletados em {:.3g}s: {}\n'
            ''
            ).format(
                time.time() - start_time,
                len(result),
            )
        )

        return result
