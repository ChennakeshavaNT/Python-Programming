# generate iteration of hanoi towers for given number of discs.
# initially, consider just 3 towers, but later on extend it to multiple towers
# transfer N discs from Tower 1 to Tower 2 using Tower 3 as empty
import sys

def status():
  for i in range(cnt_towers):
    print(tower[i])
  print("")
  return

def move(tower_from, tower_to):
  global cnt_iter

  cnt_iter = cnt_iter + 1
  tower_to.insert(0,tower_from.pop(0))
  status()
  return

def hanoi(n, t1, t2, t3):
  if (n == 1):
    move(tower[t1], tower[t2])
    return

  if (n <= aux_towers): # there are enough towers to move these discs
    # identify empty towers
    t_empty = []
    for i in range(cnt_towers):
      if not(i==t1 or i==t2):
        t_empty.append(i)
    # one each at a time from smaller to bigger
    for i in range(n):
      move(tower[t1], tower[t_empty[i]])
    # one each at a time from larger to smaller on target tower
    for i in range(n):
      move(tower[t_empty[n-1 - i]], tower[t2])
    return

  # transfer first top (n-k) discs to Tower 3 using tower 2 as empty
  hanoi(n - aux_towers, t1, t3, t2)
  # move the base k discs (equal to aux_towers)
  # identify empty towers
  t_empty = []
  for i in range(cnt_towers):
    if not(i==t1 or i==t2 or i==t3):
      t_empty.append(i)
  for i in range(aux_towers-1):
    move(tower[t1], tower[t_empty[i]])
  # move the bottom disc to t2
  move(tower[t1], tower[t2])
  # move the discs back to t2
  for i in range(aux_towers-1):
    move(tower[t_empty[aux_towers-1-1 - i]], tower[t2])
  # move n-k discs from T3 to T2 using T1 as empty
  hanoi(n - aux_towers, t3, t2, t1)

  return
#for debugging with idle IDE, use the following to pass cmd line arguments
#sys.argv = ["hanoi.py", 6, 3] For
# validation of input parameters
if (len(sys.argv) != 3):
  print("Usage: ", sys.argv[0], " <num of discs> <num of auxiliary towers>")
  exit()
try:
  cnt_discs = int(sys.argv[1])
  if (cnt_discs < 1):
    raise Exception("Number of discs should be greater than 1")
    exit()
  aux_towers = int(sys.argv[2])
  if (aux_towers < 1):
    raise Exception("Number of auxiliary towers should be greater than 1 ")
    exit()
except:
  print("Value of number of discs is improper")
  exit()

cnt_towers = aux_towers + 2
tower = [None] * cnt_towers
for i in range(cnt_towers):
  tower[i] = []

cnt_iter = 0

# initially all discs are on tower 1
for discnum in range(1,cnt_discs+1):
  tower[0].append("D" + str(discnum))


status()
hanoi(cnt_discs, 0, 1, cnt_towers - 1)
print("total moves =", cnt_iter)

