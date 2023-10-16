# Hello Toilet

## Overview
So you're telling me that you've survived the homepage, the getting started and also the installation?
You have to be my deepest fan nonetheless.
In this module we will write a simple Hello Toilet program with the use of Cacca.

## Scripting
For writing you Hello Toilet project in cacca, you'll need a few lines of code.
Cacca shines the most when you need to create huge workflows that can change from time to time.

Let's see the mock project that I've promised you:
```python
from cacca.lib import Cacca

cacca = Cacca()

cacca.insert({"action": print})
cacca.run(0, {"action": "Hello, Toilet!"})
```

Breaking this down, we import `Cacca` from its standard library and instantiate an object.
Yes you can have multiple objects and make free use of your creativity, creating multiple workflows at once.
```python
from cacca.lib import Cacca
cacca = Cacca()
```

After this, we have to just insert an action inside the pipeline.
`Actions` can be simple functions. For this project we're using print function directly from Python.
There is the possibility to add also `guards` and `hooks` that will be run respectively at the start and at the end of an action.
So if you're willing to make conditional workflows or enriched workflows, that's your best place to do that.
They have the same functionalities of an action, though.
```python
cacca.insert({"action": print})
```

When you've defined your pipeline, you can simply run it and give it, where needed, the arguments that it needs.
```python
cacca.run(0, {"action": "Hello, Toilet!"})
```

And that is all. That is **Cacca**.

## Community
If you have questions or need help, reach out to the community at [GitHub Discussions](https://github.com/airscripts/cacca/discussions).