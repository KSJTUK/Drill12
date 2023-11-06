objects = [[] for _ in range(4)]  # 보이는 세계->add_object, -> remove_object
# 실제 게임 월드를 처리할 떄는 보이는 세계와 물리적인 세계 둘 모두를 처리 해야한다.

# fill here
# 충돌의 세계->add_collision_pair
#           ->remove_collision_pair
collision_pairs = {} # {'bal:ball' : [ [ boy ], [ ball ] ] }

def add_collision_pair(groub, a=None, b=None):  # a와 b 사이에 충돌 검사가 필요하다
    if groub not in collision_pairs:
        print(f'Added new groub {groub}')
        collision_pairs[groub] = [ [] , [] ]
    if a:
        collision_pairs[groub][0].append(a)
    if b:
        collision_pairs[groub][1].append(b)


def add_object(o, depth=0):
    objects[depth].append(o)


def add_objects(ol, depth=0):
    objects[depth] += ol


def update():
    for layer in objects:
        for o in layer:
            o.update()


def render():
    for layer in objects:
        for o in layer:
            o.draw()


# fill here
def collide(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    return True


def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)



def remove_object(o):
    for layer in objects:
        if o in layer:
            # 실제 보이는 세계에서 지움
            layer.remove(o)
            # 물리적인 세계에서 지움
            remove_collision_object(o)
            # 객체 자체를 지워서 메모리를 반환
            del o
            return
    raise ValueError('Cannot delete non existing object')


def clear():
    for layer in objects:
        layer.clear()

# fill here
def handle_collisions():
    for groub, pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a, b):
                    print('COLLISION: boy : ball')
                    a.handle_collision(groub, b)
                    b.handle_collision(groub, a)