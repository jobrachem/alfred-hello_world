import alfred
import alfred.page as p
import alfred.element as e


def generate_experiment(self, path):
    hello_world = p.WebCompositePage(title="Hello, world!")
    text_entry = e.TextEntryElement("Please enter some text.")
    hello_world.append(text_entry)

    exp = alfred.Experiment()
    exp.append(hello_world)
    return exp


alfred.run(generate_experiment)
