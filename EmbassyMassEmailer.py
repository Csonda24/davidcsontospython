import pandas
dictionary = {'info.canberra@mfa.af',
'embassy.canberra@mfa.gov.al',
'info@algeriaemb.org.au',
'embangola@angolaembassy.sg',
'eaust@mrecic.gov.ar',
'canberra-ob@bmeia.gv.at',
'canberra@mission.mfa.gov.az',
'Jakarta.mission@mofa.gov.bh',
'hoc.canberra@mofa.gov.bd',
'japan@mfa.gov.by',
'canberra@diplobel.fed.be',
'ambabenjapan@gmail.com',
'st.rbe.reception@gmail.com',
'bolivianembassy@bellnet.ca',
'embassy@bihembassy.org',
'botaus-info@gov.bw',
'consular.camberra@itamaraty.gov.br',
'bruneihc@brunei.org.au',
'Embassy.Canberra@mfa.bg',
'faso-amb@khaki.plala.or.jp',
'cambodianembassy@ozemail.com.au',
'info@cameroon-embassy-jp.org',
'echile.australia@minrel.gob.cl',
'chinaemb_au@mfa.gov.cn',
'eaustralia@cancilleria.gov.co',
'mbcr-au@rree.go.cr',
'sec.australie@diplomatie.gouv.ci',
'croemb.canberra@mvep.hr',
'embajada@cubaus.net',
'info@cyprus.org.au',
'canberra@embassy.mzv.cz',
'cbramb@um.dk',
'djibouti@fine.ocn.ne.jp',
'embassyaustralia@cancilleria.gob.ec',
'egyptcanberra@gmail.com',
'embajadacanberra@rree.gob.sv',
'tseggai46@yahoo.com',
'embassy.canberra@mfa.ee',
'info@ethiopianembassy.net',
'admin@aus-fhc.org',
'sanomat.can@formin.fi',
'info@ambafrance-au.org',
'secretariat.canberra-amba@diplomatie.gouv.fr',
'gamextriyadh@yahoo.com',
'canberra.emb@mfa.gov.ge',
'info@canberra.diplo.de',
'gh57391@bigpond.net.au',
'canberra@mfa.gov.gh',
'gremb.can@mfa.gr',
'embaustralia@minex.gob.gt',
'ambaguitokyo@mae.gov.gn',
'australian.nunciature@gmail.com',
'mission.cbr@mfa.gov.hu',
'external@utn.stjr.is',
'hco.canberra@mea.gov.in',
'canberra.kbri@kemlu.go.id',
'iraq.embassy@iceiraq.org',
'canberraembassy@dfa.ie',
'info@canberra.mfa.gov.il',
'ambasciata.canberra@esteri.it',
'mail@jamaicaembassy.jp',
'economics@cb.mofa.go.jp',
'jordan@jordanembassy.org.au'
}
data_frame = pandas.DataFrame(dictionary)
data_frame.to_csv('data.csv')
import smtplib
from csv import reader
import csv
from email.mime.text import MIMEText
from time import sleep


def send(sender, pwd, reci, subject, country):
    try:
        msg = """message
"""

        msg = MIMEText(msg)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = reci

        server = smtplib.SMTP("smtp.gmail.com", 587) #put whatever smtp server you'd like here, in this case it is gmail
        server.starttls()
        server.login(sender, pwd)

        server.sendmail(sender, reci, msg.as_string())
        server.close()

    except Exception as e:
        print(str(e))
        print("Message Failed")


f = open('data.csv')
csv_f = csv.reader(f)
sendConstraint = 0 #Limit I put in to avoid sending emails to the same embassy twice. #This way emails can be done in batches/sessions instead of all at once
counter = 0

for row in csv_f:
  counter += 1
  if(counter > sendConstraint):
      subject = "About getting your countries Flag's into my currency collection"
      print("Sent message to " + row[0] + " at email : " + row[1] + " Index is " + str(counter))
      sleep(3) #Delay number I found while testing with gmail. Anything less would mess up and start skipping
