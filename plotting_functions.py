import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_xr_profile(data='xr-profile', name='X-Ray Substrate'):
    '''
    Function plots the fitted SLD profile fed to it in the arguments.
    
    Arg:
        data (str): File containing the data to be plotted
        name (str): Name of the sample, used for title and saving figure
        
    Output:
        figure: a plot of the data
    '''
    # Load data into a dataframe
    profile = pd.read_csv(f'data/{data}.dat',delim_whitespace=True,
                         usecols=['#', 'z', '(A)'])
    profile.columns = ['z','rho','irho']
    
    # Plot data and show
    
    fig, ax = plt.subplots(figsize = (11, 8.5))
    ax.plot(profile.z, profile.rho, label='rho', color='blue')
    ax.plot(profile.z, profile.irho, label='irho', color='red')
    ax.set_xlabel(r'Depth, $z$/Å')
    ax.set_ylabel(r'SLD, $\times 10^{-6}$/Å$^{2}$')
    ax.set_title(f'{name}', size=18)
    ax.legend()
    fig.savefig(f'output/{name}.pdf')

def plot_xr_refl(data='xr-refl', name='Reflectivity and Best Fit'):
    '''
    Function plots the measured reflectivity and best fit curve.
    
    Arg:
        data (str): File containing the data to be plotted
        name (str): Name of the sample, used for title and saving figure
        
    Output:
        figure: a plot of the data
    '''
    # Load data into a dataframe
    refl = pd.read_csv(f'data/{data}.dat', delim_whitespace=True,
                      usecols = ['#', 'Q', '(1/A)', 'dQ', '(1/A).1', 'R'])
    refl.columns = ['Q', 'dQ','R','dR','theory','fresnel']
    
    # Generate plot
    fig, ax = plt.subplots(figsize = (11, 8.5))
    
    ax.plot(refl.Q, refl.R, '.b', label='Reflectivity', alpha =1)
    ax.plot(refl.Q, refl.theory, '-r', label='Fitted', alpha = 0.5)
    ax.set_xlabel(r'momentum transfer, $Q_{z}\ (Å^{-1})$')
    ax.set_ylabel(r'normalized reflectivity, $R$')
    ax.set_title(f'{name}', size=18)
    
    ax.errorbar(refl.Q, refl.R, yerr=refl.dR, fmt='-', alpha=0.5)
    ax.semilogy()


def plot_pol_profile(data='polarized-profile', name='Polarized Sample'):
    '''
    Function plots the SLD profile of a polarized neutron reflectometry
    experiment.
    
    Arg:
        data (str): File containing the data to be plotted
        name (str): Name of the sample, used for title and saving figure
        
    Output:
        figure: a plot of the data
    '''
    # Load data into dataframe
    profile=pd.read_csv(f'data/{data}.dat', delim_whitespace=True,
                        usecols=["#", "z", "rho", "(1e-6/A2)"])
    profile.columns = ["z", "rho", "rhoM", "theta"]
    
    # Generate plot
    fig, ax = plt.subplots(figsize = (11, 8.5))
    ax.plot(profile.z, profile.rho, label='rho', color='blue')
    ax.plot(profile.z, profile.rhoM, label='rhoM', color='red')
    ax.set_xlabel(r'Depth, $z$/Å')
    ax.set_ylabel(r'SLD, $\times 10^{-6}$/Å$^{2}$')
    ax.set_title(f'{name}', size=18)
    ax.legend()
    fig.savefig(f'output/{name}-profile.pdf')

def plot_pol_refl(data='polarized-refl', name='Polarized Sample'):
    '''
    Function plots the reflectivity curves of a polarized neutron
    reflectometry experiment.
    
    Arg:
        data (str): File containing the data to be plotted
        name (str): Name of the sample, used for title and saving figure
        
    Output:
        figure: a plot of the data
    '''
    # Load data into dataframe--"up-up"
    refl_A = pd.read_csv(f'data/{data}.datA', delim_whitespace=True,
                        usecols=['#','Q','(1/A)','dQ', '(1/A).1', 'R'])
    refl_A.columns = ['Q','dQ','R','dR','theory','fresnel']
    
    # Load data into dataframe--"down-down"
    refl_D = pd.read_csv(f'data/{data}.datD', delim_whitespace=True,
                        usecols=['#','Q','(1/A)','dQ', '(1/A).1', 'R'])
    refl_D.columns = ['Q','dQ','R','dR','theory','fresnel']

    # Generate plot
    fig, ax = plt.subplots(figsize = (11, 8.5))
    
    ax.plot(refl_A.Q, refl_A.R, '.b', label=r'$(+,+)$', alpha =1)
    ax.errorbar(refl_A.Q, refl_A.R, yerr=refl_A.dR, fmt='-', alpha=0.5)
    ax.plot(refl_D.Q, refl_D.R, '.r', label=r'$(-,-)$', alpha =1)
    ax.errorbar(refl_D.Q, refl_D.R, yerr=refl_D.dR, fmt='-', alpha=0.5)
    
    ax.set_xlabel(r'momentum transfer, $Q_{z}\ (Å^{-1})$')
    ax.set_ylabel(r'normalized reflectivity, $R$')
    ax.set_title(f'{name}', size=18)
    ax.legend()

    ax.semilogy()
    
    fig.savefig(f'output/{name}-refl.pdf')
