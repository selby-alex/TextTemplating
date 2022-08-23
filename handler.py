import re
import itertools


def templated_cartesian_product(text):
    ## find all instances of "{ }"
    out = re.findall("(?<=)\{[^\}]*\}(?=)", text)

    ## create empty array for cartesian product
    full_opts = []

    ## iterate over found instances of "{ }"
    for inst in out:
        x = inst.replace("{", "").replace("}", "")
        opts = x.split("|")
        full_opts.append(opts)

    ## create cartesian product of all instances
    full_opts = list(itertools.product(*full_opts))

    ## convert the string to a template for replacement
    template = re.sub("(?<=)\{[^\}]*\}(?=)", "%s", text)

    ## fill the template with each instance
    for opt in full_opts:
        y = template.replace("%s", "{}", len(opt)).format(*opt)
        print(y)


if __name__ == "__main__":
    text = "The {quick|fast|slow} {brown|red} fox {jumps|leaps|stumbles} over the {lazy|sleepy} dog."
    templated_cartesian_product(text)

