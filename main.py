
from package import * # 1
#from package import subpackage # 2

#from package.subpackage.world import say # 3
#import package # 4
from package.subpackage import * # 5

if __name__ == "__main__":
    hello.say() # 1
    #subpackage.world.say() # 2
    #say() # 3
    #package.subpackage.world.say() # 4
    world.say() # 5
