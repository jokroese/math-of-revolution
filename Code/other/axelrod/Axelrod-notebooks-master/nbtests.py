"""
Script to test all notebooks execute without errors
"""
import nbformat
import pathlib
from nbconvert.preprocessors import ExecutePreprocessor

def retrieve_errors(nb_path):
    """
    Find all errors that occur when running a nb
    """

    with nb_path.open() as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=600, kernel_name='python3',
                             allow_errors=True)
    out, _ = ep.preprocess(nb, {'metadata': {'path': '.'}})
    errors = []
    for cell in out.cells:
        if "outputs" in cell:
            for output in cell["outputs"]:
                if output.output_type == "error":
                    errors.append(output.evalue)
    return errors

if __name__ == "__main__":

    nb_dir = pathlib.Path('.')
    nbs = nb_dir.glob("*.ipynb")

    for path in nbs:
        print("Testing: {}".format(path.stem))
        errors = retrieve_errors(path)
        assert errors == [], errors
