---
permalink: /
title: "Biography"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
I am a Ph.D. student in [Paul G. Allen school of Computer Science and Engineering](https://www.cs.washington.edu/) at [University of Washington](https://www.washington.edu/). I am a member of [MELODI lab](https://melodi.ece.uw.edu/), advised by [Prof. Jeff A. Bilmes](https://people.ece.uw.edu/bilmes/p/pgs/index.html). My research interests are in machine learning, optimization, and natural language processing. I have published ~50 papers at NeurIPS, ICML, ICLR, AISTATS, NAACL, COLING, KDD, ICDM, AAAI, IJCAI, ISIT, Machine Learning (Springer), IEEE TIP, IEEE TNNLS, IEEE TKDE, etc. I am the recipient of the Best Student Paper Award at ICDM 2013 and the 2020 IEEE Computer Society Technical Committee on Scalable Computing (TCSC) Most Influential Paper Award.

I have been a research assistant at [University of Technology, Sydney (UTS)](https://www.uts.edu.au/) and [Nanyang Technological University (NTU)](https://www.ntu.edu.sg/Pages/home.aspx), supervised by [Prof. Dacheng Tao](https://www.sydney.edu.au/engineering/about/our-people/academic-staff/dacheng-tao.html). I was a research intern at [Yahoo! Labs](https://research.yahoo.com/), supervised by [Hua Ouyang](https://www.linkedin.com/in/hua-ouyang-5869b851) and [Yi Chang](http://www.yichang-cs.com/), and a research intern at [Microsoft Research](https://www.microsoft.com/en-us/research/), supervised by [Lin Xiao](https://linxiaolx.github.io/). 
<!-- My collaborators also include members from [Chengqi Zhang](https://profiles.uts.edu.au/Chengqi.Zhang) and [Guodong Long](https://profiles.uts.edu.au/Guodong.Long)'s groups in [Australian AI Institute](https://www.uts.edu.au/research-and-teaching/our-research/australian-artificial-intelligence-institute) at University of Technology, Sydney, and [Meng Fang](https://mengf1.github.io/) at Tencent AI Lab. -->

My Research
------
* Machine Learning
  1. Curriculum Learning (for 2-6 below, using tools in 7-8)
  1. Self-supervised/Semi-supervised Learning
  1. Reinforcement Learning 
  1. Collaborative Learning, Ensemble Method
  1. Robust Learning on Noisy Data
  1. Meta-Learning, Few-shot/Zero-shot Learning
  1. Training Dynamics and Geometry of Neural Networks
  1. Continuous-discrete Optimization, Submodular Optimization
  1. Spectral Method for Matrix Factorization and Graphical Models
  1. Matrix Factorization: Low-rank Approximation, Robust PCA, NMF
  1. Compressed Sensing, Sparse Learning
  1. Dimension Reduction, Manifold Learning

* Natural Language Processing
  1. Attention Models
  1. Natural Language Inference
  1. Semantic Role Labeling
  1. Link Prediction in Knowledge Graphs
  1. Text Classification
  1. Summarization

News
------
* 2020/09: One paper has been accepted to NeurIPS 2020.
* 2020/06: One paper has been accepted to ICML 2020.

<script type="text/javascript" id="clstr_globe" src="//clustrmaps.com/globe.js?d=yS55EhS2ol9nZNevQxAHb2-_nUUI3Opt9QjGnAYIFrg"></script>

<!-- Getting started
======
1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
1. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section

Site-wide configuration
------
The main configuration file for the site is in the base directory in [_config.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_config.yml), which defines the content in the sidebars and other site-wide features. You will need to replace the default variables with ones about yourself and your site's github repository. The configuration file for the top menu is in [_data/navigation.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_data/navigation.yml). For example, if you don't have a portfolio or blog posts, you can remove those items from that navigation.yml file to remove them from the header. 

Create content & metadata
------
For site content, there is one markdown file for each type of content, which are stored in directories like _publications, _talks, _posts, _teaching, or _pages. For example, each talk is a markdown file in the [_talks directory](https://github.com/academicpages/academicpages.github.io/tree/master/_talks). At the top of each markdown file is structured data in YAML about the talk, which the theme will parse to do lots of cool stuff. The same structured data about a talk is used to generate the list of talks on the [Talks page](https://academicpages.github.io/talks), each [individual page](https://academicpages.github.io/talks/2012-03-01-talk-1) for specific talks, the talks section for the [CV page](https://academicpages.github.io/cv), and the [map of places you've given a talk](https://academicpages.github.io/talkmap.html) (if you run this [python file](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.py) or [Jupyter notebook](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb), which creates the HTML for the map based on the contents of the _talks directory).

**Markdown generator**

I have also created [a set of Jupyter notebooks](https://github.com/academicpages/academicpages.github.io/tree/master/markdown_generator
) that converts a CSV containing structured data about talks or presentations into individual markdown files that will be properly formatted for the academicpages template. The sample CSVs in that directory are the ones I used to create my own personal website at stuartgeiger.com. My usual workflow is that I keep a spreadsheet of my publications and talks, then run the code in these notebooks to generate the markdown files, then commit and push them to the GitHub repository.

How to edit your site's GitHub repository
------
Many people use a git client to create files on their local computer and then push them to GitHub's servers. If you are not familiar with git, you can directly edit these configuration and markdown files directly in the github.com interface. Navigate to a file (like [this one](https://github.com/academicpages/academicpages.github.io/blob/master/_talks/2012-03-01-talk-1.md) and click the pencil icon in the top right of the content preview (to the right of the "Raw | Blame | History" buttons). You can delete a file by clicking the trashcan icon to the right of the pencil icon. You can also create new files or upload files by navigating to a directory and clicking the "Create new file" or "Upload files" buttons. 

Example: editing a markdown file for a talk
![Editing a markdown file for a talk](/images/editing-talk.png)

For more info
------
More info about configuring academicpages can be found in [the guide](https://academicpages.github.io/markdown/). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful.
 -->