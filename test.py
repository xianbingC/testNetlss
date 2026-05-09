def entry(opt=None):
  channels['COM'].iocmd('SetConfig',{'baudrate':110})
  msg = channels['COM'].iocmd('GetConfig')
  print(str(msg))
  print('此处输入程序代码')
  1111
