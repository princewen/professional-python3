registry=[]

def register(decorated):
    registry.append(decorated)
    return decorated


#相当于先执行了foo=register(foo)
@register
def foo():
    return 3
#相当于先执行了bar=register(bar)
@register
def bar():
    return 5


#如果调整位置，answers和registry都是空
answers=[]
for func in registry:
    answers.append(func())
print (registry)
print (answers)