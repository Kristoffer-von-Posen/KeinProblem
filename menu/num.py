from menu.models import Btwo

x = 1

for word in Btwo.objects.all():

  word.qnu = x
  word.save()

  if (x < 30):
    x = x + 1
  else:
    x = 1
