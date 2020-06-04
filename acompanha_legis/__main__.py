#!/bin/python3

if __package__ is None or __package__ == '':
    from acompanha_legis import AcompanhaLegis
else:
    from acompanha_legis.acompanha_legis import AcompanhaLegis

import argparse
import json
from datetime import date


def create_parser():
    parser = argparse.ArgumentParser(
        description='Acompanha Legis - Solução automatizada '
                    'de acompanhamento legislativo'
    )
    parser.add_argument(
        '-d', '--dep',
        required=True,
        help='Nome completo do deputado(a).',
        type=str,
    )
    parser.add_argument(
        '-a', '--ano',
        required=False,
        help='Ano das proposições.',
        default=date.today().strftime('%Y'),
        type=int,
    )
    parser.add_argument(
        '-n', '--numero',
        required=False,
        help='Número da proposição.',
        type=int,
    )
    parser.add_argument(
        '-o', '--output',
        required=False,
        help='Camido do arquivo para output',
        type=str,
    )
    return parser


def main():
    args = create_parser().parse_args()
    dep = args.dep
    ano = args.ano
    num = args.numero
    o = args.output

    print(
        str(
            '\nDep.: {}\n'
            'Ano das proposições: {}'
        ).format(
            dep,
            ano,
        )
    )

    if num:
        print(
            'Proposição: {}'.format(
                num,
            )
        )

    data = AcompanhaLegis(
        dep,
        ano,
    ).main()

    if o:
        with open('{}/{}.json'.format(o, dep.replace(' ', '_')), 'w') as f:
            json.dump(data, f, ensure_ascii=False)

    if num and data:
        for d in data:
            if d.get('numero') == num:
                print(
                    json.dumps(d, indent=3, ensure_ascii=False)
                )
                break


if __name__ == '__main__':
    main()
