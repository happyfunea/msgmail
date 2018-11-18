#!/usr/bin/python
#-*-coding:utf-8-*-
'''Tinggal Make Aja Bro'''
'''Gausah Recode Hehe'''
W = '\033[1;37m' # White bold
N  = '\033[0m'  # white (Normal)
R = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
import smtplib,sys,subprocess as a
_banner_ = '''                                          _  _  
                                         (_)| | 
 ____    ___   ____  _____  ____   _____  _ | | 
|    \  /___) / _  |(_____)|    \ (____ || || | 
| | | ||___ |( (_| |       | | | |/ ___ || || | 
|_|_|_|(___/  \___ |       |_|_|_|\_____||_| \_)
             (_____|            
\033[34m-----\033[33mINFO\033[34m-----
\033[1;32mAbout Program\033[0m : Send'ing Message to gmail Power Full By AgoOeng
\033[1;32mAuthor\033[0m : \033[0mAgoOeng
\033[1;32mCodedName\033[0m  : \033[0m[@9un9]
\033[1;32mTeam\033[0m : CRABS
\033[34m-----\033[33mclose-info\033[34m-----'''

class _gml_():
	def __init__(self):
		try:
			self.us = raw_input(G+'Your Email'+N+': ')
			self.pw = raw_input(G+'Your Password'+N+': ')
			self.trgt = raw_input(G+'Email Target'+N+': ')
			self.msg = raw_input(B+'Your Pesan'+N+': ')
			self.lmt = raw_input(B+'Limit'+N+': ')
		except:
			print '\n'
			print R+'[!]'+N+'Check Your Password/Email Target \n[*]Check Your Connection!'
			sys.exit
		self.count = 0
		while (int(self.lmt)>self.count):
			try:
				self.server = smtplib.SMTP('smtp.gmail.com', 587)
				self.server.starttls()
				self.server.login(self.us, self.pw)
				self.pesan = self.msg
				self.server.sendmail(self.us, self.trgt, self.pesan)
				self.count=self.count+1
				self.server.quit()
				print '__________________________'
				print R+'[*]'+G+'Succes'+N+':'+B+' Send To Gmail'+N+'>> '+self.trgt
				print R+'[*]'+G+'Message'+N+':'+self.msg
				print '__________________________'
			except Exception as a:
				try:
					print '__________________________'
					print R+'[!]'+G+'Failed'+N+':'+B+' Send To Email'+N+'>>'+self.trgt
					print '__________________________'
					sys.exit()
				except:
					print '--------------------------'
					print R+'[!]'+G+'Gagal'+N+':'+B+' Mengirim Ke'+N+'>>'+self.trgt
					print '--------------------------'
					print R+'+-------------------------------'+G+'EROR'+R+'----------------------------+'+B
					print 'Check Your Connection Internet!/Username And Password\nOr Email Target Not Ivalid!'
					print R+'+---------------------------------------------------------------+'

					sys.exit()
if __name__=='__main__':
        a.call('clear', shell=True)
	print _banner_
	_gml_()
	print R+ '[!]'+B+'Spam Finished!'
