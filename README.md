# logSing
This repository contains commented Jupyter Notebooks and LaTeX files used to
generate figures in the manuscript titled ``Entropic singularities
give rise to quantum transmission``. These files are briefly described below

----------
LaTeX Files
----------
Both LaTeX files described below can be compiled using standard LaTeX software
to generate pdf files, FigA.pdf and FigB.pdf, included in this directory.

FigA.tex
----------
Generates Figure 2 (FigA.pdf), a schematic for the reason behind an log-singularity

FigB.tex
----------
Generates Figure 4 (FigB.pdf) representing an incomplete erasure channel


----------
Jupyter Notebooks
----------
All three Jupyter Notebooks and a supporting Python function file described
below can be reviewed using standard Jupyter Notebook and word processing
software, respectively. The notebooks use standard Python packages (for
instance see requirements.txt) and the supporting Python function file but are
otherwise standalone documents which quickly generate three plots Fig3LS.pdf,
Fig3Diff.pdf, and FigD.pdf in Figures 1, 3, and 5, respectively. 

Fig3LS.ipynb        
----------
Generates Figure 1 (Fig3LS.pdf), behaviour of the von-Neumann entropy in the
vicinity of an epsilon log-singularity.

Fig3LSDiff.ipynb
----------
Generates Figure 3 (Fig3LSDiff.pdf), illustration of log-singularity based
mechanism behind positivity of the channel coherent information.

FigD.ipynb
----------
Generates Figure 5 (FigD.pdf), non-additivity in a low-noise channel.

helperFun.py
----------
Contains simple functions useful for computations in Fig3LS, Fig2LSDiff, and
FigD files above.
