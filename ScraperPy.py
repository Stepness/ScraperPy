import requests
import lxml.html

def Find_tot_equity(stock_code, year) -> float:
    stock_codeNoMarket = stock_code.split(".")[0]

    html = requests.get("http://quote.cfi.cn/" + stock_codeNoMarket + ".html")
    doc = lxml.html.fromstring(html.content)

    #Tiro fuori la riga dell'header della tabella 
    DeadlineRow = doc.xpath('/html/body/form/table[1]/tr[2]/td[3]/div[2]/table/tr[6]/td/table/tr/td[1]/table/tr[1]//text()')

    DeadlineIndex = 0

    #Cerco nell'header l'indice della colonna che ha l'anno di cui ho bisogno
    for idx, Deadline in enumerate(DeadlineRow):
        if Deadline == (year + "年12-31"):
            DeadlineIndex = idx
            break

    TotalEquityRow = doc.xpath('/html/body/form/table[1]/tr[2]/td[3]/div[2]/table/tr[6]/td/table/tr/td[1]/table/tr[2]//text()')

    return float(TotalEquityRow[DeadlineIndex])*(10**8)

    