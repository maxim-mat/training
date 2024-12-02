import nbformat

# Load the first notebook
with open('/Users/shalevhabany/Desktop/devl/CV_training/basic/python/data_visualization/data_visualization.ipynb', 'r') as f:
    nb1 = nbformat.read(f, as_version=4)

# Load the second notebook
with open('/Users/shalevhabany/Desktop/devl/CV_training/basic/python/data_visualization/data_visualization_tmp.ipynb', 'r') as f:
    nb2 = nbformat.read(f, as_version=4)

# Concatenate the cells from the second notebook to the first
nb1.cells.extend(nb2.cells)

# Save the merged notebook
with open('/Users/shalevhabany/Desktop/devl/CV_training/basic/python/data_visualization/merged_notebook.ipynb', 'w') as f:
    nbformat.write(nb1, f)

print("Notebooks merged successfully!")