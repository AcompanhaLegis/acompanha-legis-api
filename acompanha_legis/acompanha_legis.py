import json
import re
import requests
from datetime import datetime


class AcompanhaLegis():
    d = {
        'host': 'https://dadosabertos.camara.leg.br/api/v2'
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

    def get_temas(self, id):
        d = {}
        res = requests.get(
            '{}/proposicoes/{}/temas'.format(
                self.d.get('host'),
                id,
            ),
            stream=True
        ).json()

        if len(res.get('dados', [])) > 0:
            d = {
                'temas': []
            }
            for data in res['dados']:
                d['temas'].append(
                    data['tema']
                )

        return d

    def get_tram(self, id):
        d = {}
        res = requests.get(
            '{}/proposicoes/{}/tramitacoes'.format(
                self.d.get('host'),
                id,
            ),
            stream=True
        ).json()

        if len(res.get('dados', [])) > 0:
            com = []
            d = {
                'ultima_movimentacao': [],
            }

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

                com.append(
                    tram.get('siglaOrgao')
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

        return d

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

    def do_data(self, dep_id):
        data = []
        tpl = {
            'ano': 0,
            'proposicao': '',
            'numero': 0,
            'apresentacao': '',
            'ementa': '',
            'temas': '',
            'apreciacao': '',
            'tramitacao': '',
            'comissao_destinado': '',
            'comissao_atual': '',
            'apensado': '',
            'relator': '',
            'ultima_movimentacao': '',
            'link': '',
        }

        count = 0
        props = self.get_prop(
            dep_id
        )

        for id in props:
            print(
                '{0:.0%} '.format(
                    count/len(props)
                ),
                end='',
                flush=True
            )

            d = tpl.copy()

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

            d = {
                **d,
                **self.get_temas(id),
                **self.get_tram(id),
            }

            data.append(d)

            count += 1

        return data

    def main(self):
        print(
            '\nColetando dados...'
        )

        result = self.do_data(
            self.d.get('id')
        )

        print(
            '\n\nDados coletados: {}\n'.format(
                len(result)
            )
        )

        return result
