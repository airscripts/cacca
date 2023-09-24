from cacca.lib import Cacca

cacca = Cacca()

cacca.insert({"action": print})
cacca.run(0, {"action": "Hello, Toilet!"})
