def exeOperation(cmd):
    print 'Espressione:'+ cmd
    a=''
    check=1
    r=0.0
    try:
      if cmd.find('+')>-1:
        a=cmd.split('+')
        r=long(a[0])+long(a[1])
      elif cmd.find('-')>-1:
        a=cmd.split('-')
        r=long(a[0])-long(a[1])
      elif cmd.find('/')>-1:
        a=cmd.split('/')
        r=float(a[0])/float(a[1])
      elif cmd.find('x')>-1:
        a=cmd.split('x')
        r=long(a[0])*long(a[1])
      elif cmd.find('*')>-1:
        a=cmd.split('*')
        r=long(a[0])*long(a[1])
      elif cmd.find('^')>-1:
        a=cmd.split('^')
        r=pow(long(a[0]),long(a[1]))
       
    except Exception as e:
      check=0
      print e

    finally:
      if check==1:
        return str(r)
      else:
        return 'Non riesco ad eseguire il calcolo!'
