import pdfplumber
import re
from pandas import DataFrame
import json
import sys


def matching(standard,text,position):
    match=re.search(standard,text)
    if match:
        valor=match.group(int(position))
    else:
        valor=""
    return valor

def get_data(path):
    try:
        with pdfplumber.open(path) as pdf:

            pages=pdf.pages
            all_text=''
            for p in pages:
                text=p.extract_text()
                all_text=all_text+'\n'+text

        faturas=all_text.split("NOTA FISCAL DE SERVIÇOS DE TELECOMUNICAÇÕES")

        CNPJ_tomador=matching(r'CPF\/CNPJ.(\d{14})',faturas[0],1)
        CNPJ_tomador=CNPJ_tomador.strip()

        del faturas[0]

        cnpjs_emissor=[]
        razoes_sociais=[]
        nfsts=[]
        n_series=[]
        emissoes=[]
        valores_totais=[]
        cnpjs_tomador=[]
        icms_global=[]
        cfops=[]

        for fatura in faturas:
            CNPJ_emissor=matching(r'CNPJ:\s*(\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2})',fatura,1)
            CNPJ_emissor=CNPJ_emissor.strip()
            
            razao_social=matching(r'Nome da Empresa:\s*(.*)\s*Nº NFST:',fatura,1)
            razao_social=razao_social.strip()

            nro_nfst=matching(r'Nº NFST:\s*(.*)\s*Nº Série:',fatura,1)
            nro_nfst=nro_nfst.strip()

            nro_serie=matching(r'Nº Série:\s*(\w*)',fatura,1)
            nro_serie=nro_serie.strip()

            emissao=matching(r'Emissão:\s*(\d{2}.\d{2}.\d{4})',fatura,1)
            emissao=emissao.strip()

            valor_total=matching(r'TOTAL NOTA FISCAL\s*\D*(\d*\.*\d*,\d{2})',fatura,1)
            valor_total=valor_total.strip()

            valor_cfop=matching(r'CFOP\s*.*(\d{1}.\d{3})',fatura,1)
            valor_cfop=valor_cfop.strip()


            icms_list=re.findall(r'(ICMS|PIS|COFINS)\s*(\d*\,*\d+%)\s*Base de Cálculo\s*(R\$\s+\d*\.*\d+,\d+)\s+Valor\s*(?:ICMS|PIS|COFINS)\s*(R\$\s+\d*\.*\d+,\d+)\s+Ser\.Isentos/Não Tributável\s*(R\$\s+\d*\.*\d+,\d+)',fatura)

            for l in icms_list:
                l2=list(l)
                l2.append(CNPJ_emissor)
                l2.append(razao_social)
                l2.append(nro_nfst)
                l2.append(nro_serie)
                l2.append(emissao)
                l2.append(valor_total)
                l2.append(CNPJ_tomador)
                l2.append(valor_cfop)
                icms_global.append(l2)
        


        df = DataFrame (icms_global,columns=['IMPOSTO','ALIQUOTA','BASE_DE_CALCULO','VALOR_IMPOSTO','Nao_Tributavel','CNPJ_emissor','razao_social','nro_nfst','nro_serie','emissao','valor_total','CNPJ_tomador','CFOP'])
        JSONstring = df.to_json(orient='records')
        status=JSONstring
    
    except Exception as e:
        status=e


    print(status)
    return status


#Pass the path of the PDF as variable and Script will extract Data from It as indicated on Df. Works for Claro PDF invoices only

if __name__ == "__main__":
    path = sys.argv[1]
    get_data(path)
