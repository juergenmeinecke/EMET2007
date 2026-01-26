Get Python-ready!
=================

Why coding in econometrics?
---------------------------

Econometrics is all about using data to answer real-world economic questions. To do this well, we
need to be able to work with data—loading it, cleaning it, visualising it, and running statistical
analyses on it.

While you could do some of this in spreadsheets, modern econometric work involves datasets and
methods that quickly outgrow what Excel can handle. That's where coding comes in. Writing code lets
you automate repetitive tasks, handle large datasets, reproduce your analysis exactly, and apply
sophisticated statistical techniques.

Don't worry if you've never coded before! We'll be using Python, which is known for being
beginner-friendly and readable. And rather than writing code in a scary black terminal window, we'll
use Jupyter notebooks—a friendly environment where you can write code, see results, and add notes
all in one place, right in your web browser.

Think of it as a digital lab notebook for data work.


What are Python and Jupyter?
----------------------------

What is `Python <https://python.org>`_!? Well, Python's awesome! Enough said.

We will be using Python for our econometric data work. The way we interact with Python is through
so-called Jupyter notebooks. Our friends from `quantecon.org <https://quantecon.org>`_ clarify:

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

Google Colab is free and lets you run Jupyter notebooks in your browser without installing anything. You will need a Google account (any Gmail account works).

.. note::

   - Make sure you're logged into the correct Google account if you have multiple.
   - When connecting Colab to Drive, a pop-up will ask you to grant permissions -- click **Allow** for all permissions.
   - If you accidentally click "Deny", just run the cell again.

**Step 1: Clone the Repository to Google Drive**

1. Go to `colab.research.google.com <https://colab.research.google.com>`_
2. Click **New notebook**
3. In the first cell, type:

   .. code-block:: python

      from google.colab import drive
      drive.mount('/content/drive')

4. Press **Shift + Enter** to run the cell
5. Click the link that appears, sign in to your Google account, and grant access
6. In the next cell, type:

   .. code-block:: python

      %cd /content/drive/MyDrive
      !git clone https://github.com/juergenmeinecke/EMET2007.git

7. Press **Shift + Enter** to run the cell

**Step 2: Access Your Files**

1. Go to `drive.google.com <https://drive.google.com>`_
2. You should see a folder called **EMET2007**
3. Open the folder and double-click any ``.ipynb`` file
4. Choose **Open with** -> **Google Colaboratory**

If you don't see Google Colaboratory as an option, click **Connect more apps**, search for "Colaboratory", and install it.

**Updating the Repository Later**

Open any Colab notebook and run:

.. code-block:: python

   from google.colab import drive
   drive.mount('/content/drive')
   %cd /content/drive/MyDrive/EMET2007
   !git pull

If you get an error about local changes:

.. code-block:: python

   %cd /content/drive/MyDrive/EMET2007
   !git checkout .
   !git pull


Anaconda
--------

Anaconda is the world's most popular open-source Python distribution platform. You can download a free version from `anaconda.com/download <https://www.anaconda.com/download/>`_.

This will install a rich Python environment on your computer including:

- The Python programming language (with all the libraries you will need)
- The Jupyter notebooks environment
- Many other tools to take your Python programming further

The installation process is straightforward -- just download the installer for your operating system and follow the prompts.

**Launching Jupyter**

After installation, you can launch Jupyter in several ways:

- **Anaconda Navigator**: Open Anaconda Navigator and click **Launch** under Jupyter Notebook (recommended for beginners)
- **Windows**: Type "Jupyter" in your search bar
- **Mac**: Search for "Jupyter" using Spotlight (Cmd + Space)
- **Command line**: Open a terminal or Anaconda Prompt and type ``jupyter notebook``

.. warning::

   Do not launch ``.ipynb`` files by double-clicking them in your File Explorer or Finder! This will not work correctly. Always open Jupyter first, then navigate to your files.

**Windows Users**

*Install Git:*

1. Open **Anaconda Prompt** (search for it in the Start menu)
2. Type the following command and press Enter:

   .. code-block:: bash

      conda install git

3. When prompted, type ``y`` and press Enter to confirm
4. Wait for the installation to complete

*Clone the Repository:*

1. Open **Anaconda Navigator** (search for it in the Start menu)
2. Click **Launch** under Jupyter Notebook
3. In Jupyter, click **New** -> **Python 3** (top right) to create a new notebook
4. In the first cell, type:

   .. code-block:: python

      !git clone https://github.com/juergenmeinecke/EMET2007.git

5. Press **Shift + Enter** to run the cell
6. Wait for the download to complete

*Access Your Files:*

1. Click the **Jupyter** logo in the top left to return to the file browser
2. You should see a new folder called **EMET2007**
3. Open the folder and click on any ``.ipynb`` file to start working

**Mac Users**

*Clone the Repository:*

Git is usually pre-installed on Mac, so you can skip straight to cloning.

1. Open **Anaconda Navigator** (search for it using Cmd + Space)
2. Click **Launch** under Jupyter Notebook
3. In Jupyter, click **New** -> **Python 3** (top right) to create a new notebook
4. In the first cell, type:

   .. code-block:: python

      !git clone https://github.com/juergenmeinecke/EMET2007.git

5. Press **Shift + Enter** to run the cell
6. If prompted to install command line developer tools, click **Install** and wait for it to finish, then run the cell again

*Access Your Files:*

1. Click the **Jupyter** logo in the top left to return to the file browser
2. You should see a new folder called **EMET2007**
3. Open the folder and click on any ``.ipynb`` file to start working


Updating the Repository (Anaconda)
----------------------------------

If the repository gets updated and you want the latest version:

1. Open any notebook
2. Run this command:

   .. code-block:: python

      %cd EMET2007
      !git pull

If you get an error about local changes:

.. code-block:: python

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
