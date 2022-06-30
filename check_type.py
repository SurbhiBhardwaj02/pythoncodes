
def typee(x):
    if type(x) is tuple:
        print('tuple')
    if type(x) is list:
        print('list')
    if type(x) is set:
        print('set')

typee({2,3,55,'vv',66,3})
typee([2,4,5,'t',2])
typee((3,4,5,'tt'))
   