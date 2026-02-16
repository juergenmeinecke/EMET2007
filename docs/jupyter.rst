Get Python-ready!
=================

What are Python and Jupyter?
----------------------------

Econometrics is all about using data to answer real-world economic questions. To do this well, we
need to be able to work with data—loading it, cleaning it, visualising it, and running statistical
analyses on it.

While you could do some of this in spreadsheets, modern econometric work involves datasets and
methods that quickly outgrow what Excel can handle. That's where coding comes in. 
We'll be doing all our coding in Python. Don't worry if you've never coded before, we'll teach
everything from scratch.

What is `Python <https://python.org>`_!? Well, Python's awesome! Enough said.  The way we interact
with Python is through so-called **Jupyter notebooks**. Our friends from `quantecon.org
<https://quantecon.org>`_ explain:

.. admonition:: What are Jupyter notebooks?

    Jupyter notebooks are one of the many possible ways to interact with Python and the scientific
    libraries.

    They use a browser-based interface to Python with

    * The ability to write and execute Python commands.

    * Formatted output in the browser, including tables, figures, animation, etc.

    * The option to mix in formatted text and mathematical expressions.

    Because of these features, Jupyter is now a major player in the scientific computing ecosystem.

    (referenced from `here <https://python-programming.quantecon.org/getting_started.html#jupyter-notebooks>`_)

Yes, you heard that right: Jupyter notebooks allow you to run Python inside a web browser!

I hear you ask: Sounds awesome, but how in the world do I get started with Jupyter!? Well, two options:

1. **Cloud based**: Google Colab
2. **Local install**: Anaconda

I will explain these two in the next sections.

.. note::

   There are other ways to run Python and Jupyter notebooks that we won't cover here, including:

   - `Binder <https://mybinder.org>`_ -- launches Jupyter notebooks directly from a GitHub repository
   - `GitHub Codespaces <https://github.com/features/codespaces>`_ -- a full development environment in the cloud
   - `JupyterHub <https://jupyter.org/hub>`_ -- often used by universities to provide shared Jupyter servers
   - `VS Code <https://code.visualstudio.com>`_ -- a popular code editor with excellent Jupyter support
   - `JupyterLab <https://jupyterlab.readthedocs.io>`_ -- a more advanced interface (included with Anaconda)

   Feel free to explore these if you're curious, but Colab or Anaconda will serve you well for this course.


Google Colab
------------

With Colab you are essentially running Python in a Jupyter notebook on a remote (cloud) computer
provided by Google. For small applications (such as ours) this is free of charge. You do, however,
need a Google account (any Gmail account works).

The way you access this cloud computer is through your web browser.  With Colab there is no need to
install anything, you can run Python from anywhere (provided a stable internet connection).

Because it all works remotely via your web browser you can run Jupyter notebooks in many different
ways: from the university computers, your laptop, your desktop at home, your iPad, your Samsung
Galaxy, iPhone 18, Nokia 6110, Commodore 64, Nintendo Switch, you get the point.

Overview
^^^^^^^^

We explain here how you can use Colab to clone (import) the EMET2007 Github repository into your
Google Drive. After you've done that, it will be easy to use Colab to work on your EMET projects
(the details will then be explained in your week 2 computer lab).

Take a look at the Github repo: https://github.com/juergenmeinecke/EMET2007. A lot of information is
stored there including:

* weekly computer labs 
* homework assignments
* weekly lecture notes
* and much more

Clone the EMET2007 Repo to Google Drive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   - Make sure you're logged into the correct Google account if you have multiple.
   - When connecting Colab to Drive, a pop-up will ask you to grant permissions -- click **Allow** for all permissions.
   - If you accidentally click "Deny", just run the cell again.


1. Go to `colab.research.google.com <https://colab.research.google.com>`_
2. Click **New notebook**
3. In the first cell, type:

   .. code-block:: bash

      from google.colab import drive
      drive.mount('/content/drive')

4. Press **Shift + Enter** to run the cell
5. Click the link that appears, sign in to your Google account, and grant access
6. In the next cell, type:

   .. code-block:: bash

      %cd /content/drive/MyDrive
      !git clone https://github.com/juergenmeinecke/EMET2007.git

7. Press **Shift + Enter** to run the cell

   This will take a little bit of time. At the end you will have the entire EMET2007 Github repo
   stored into your Google Drive. Now you're ready to work with Python!

Accessing Your Files
^^^^^^^^^^^^^^^^^^^^

1. Go to `drive.google.com <https://drive.google.com>`_
2. You should see a folder called **EMET2007**
3. Navigate to the **computer_labs** directory, that's where the weekly computer labs are located.
4. Double-click any ``.ipynb`` file
5. Choose **Open with** -> **Google Colaboratory**
6. In the week 2 lab we will open the **week_2.ipynb** file and work on it together

If you don't see Google Colaboratory as an option, click **Connect more apps**, search for "Colaboratory", and install it.

Updating the Repo Later
^^^^^^^^^^^^^^^^^^^^^^^

Open any Colab notebook and run:

.. code-block:: bash

   from google.colab import drive
   drive.mount('/content/drive')
   %cd /content/drive/MyDrive/EMET2007
   !git pull

If you get an error about local changes:

.. code-block:: bash

   %cd /content/drive/MyDrive/EMET2007
   !git checkout .
   !git pull


Anaconda
--------

If you are the type of person who likes to run things on their own machine then you can use the
Anaconda platform to install Python and Jupyter on your computer (ideally your laptop that you bring
along to the weekly labs). This will work on PC, Mac, and Linux. (Linux really is the way to go, by
the way.)

Installing Anaconda
^^^^^^^^^^^^^^^^^^^

Anaconda is the world's most popular open-source Python distribution platform. You can download
a free version from `anaconda.com/download <https://www.anaconda.com/download/>`_.

This will install a rich Python environment on your computer including:

- The Python programming language (with all the libraries you will need)
- The Jupyter notebooks environment
- Many other tools to take your Python programming further

The installation process is straightforward -- just download the installer for your operating system
and follow the prompts.

Launching Jupyter
^^^^^^^^^^^^^^^^^

After installation, you can launch Jupyter in several ways:

- **Anaconda Navigator**: Open Anaconda Navigator and click **Launch** under Jupyter Notebook (recommended for beginners)
- **Windows**: Type "Jupyter" in your search bar
- **Mac**: Search for "Jupyter" using Spotlight (Cmd + Space)
- **Command line**: Open a terminal or Anaconda Prompt and type ``jupyter notebook``

.. warning::

   Do not launch ``.ipynb`` files by double-clicking them in your File Explorer or Finder! This will not work correctly. Always open Jupyter first, then navigate to your files.


Clone the EMET2007 Repo
^^^^^^^^^^^^^^^^^^^^^^^

**Windows Users**

*Install Git:*

1. Open **Anaconda Prompt** (search for it in the Start menu)
2. Type the following command and press Enter:

   .. code-block:: bash

      conda install git

3. When prompted, type ``y`` and press Enter to confirm
4. Wait for the installation to complete

*Clone the Repo*

1. Open **Anaconda Navigator** (search for it in the Start menu)
2. Click **Launch** under Jupyter Notebook
3. In Jupyter, click **New** -> **Python 3** (top right) to create a new notebook
4. In the first cell, type:

   .. code-block:: bash

      !git clone https://github.com/juergenmeinecke/EMET2007.git

5. Press **Shift + Enter** to run the cell
6. Wait for the download to complete

*Access Your Files:*

1. Click the **Jupyter** logo in the top left to return to the file browser
2. You should see a new folder called **EMET2007**
3. Open the folder and click on any ``.ipynb`` file to start working

**Mac Users**

*Clone the Repo*

Unlike on Windows, Git is usually pre-installed on Mac, so you can skip straight to cloning.

1. Open **Anaconda Navigator** (search for it using Cmd + Space)
2. Click **Launch** under Jupyter Notebook
3. In Jupyter, click **New** -> **Python 3** (top right) to create a new notebook
4. In the first cell, type:

   .. code-block:: bash

      !git clone https://github.com/juergenmeinecke/EMET2007.git

5. Press **Shift + Enter** to run the cell
6. If prompted to install command line developer tools, click **Install** and wait for it to finish, then run the cell again

*Access Your Files:*

1. Click the **Jupyter** logo in the top left to return to the file browser
2. You should see a new folder called **EMET2007**
3. Open the folder and click on any ``.ipynb`` file to start working


Updating the Repo
-----------------

If the repository gets updated and you want the latest version:

1. Open any notebook
2. Run this command:

   .. code-block:: bash

      %cd EMET2007
      !git pull

If you get an error about local changes:

.. code-block:: bash

   %cd EMET2007
   !git checkout .
   !git pull


Troubleshooting
---------------

**"git is not recognized" (Windows)**

You need to install Git first. Open Anaconda Prompt and run:

.. code-block:: bash

   conda install git

**"xcrun: error: invalid active developer path" (Mac)**

You need to install command line tools. Open Terminal and run:

.. code-block:: bash

   xcode-select --install

**"fatal: destination path already exists"**

You already have a folder with that name. Either delete it first or pull updates instead of cloning again.

**Google Colaboratory not showing in Drive**

Go to Google Drive -> click **New** -> **More** -> **Connect more apps** -> search for "Colaboratory" -> **Install**
