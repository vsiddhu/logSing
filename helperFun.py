
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

def entropy(p, base = 2.):
    r"""Takes as input a 1-d numpy array and base, returns the Shannon entropy 
    in given base. 
    
    Parameters
    ----------
    p : numpy array
        1-d array 
    
    base : float
           Base for the log
    
    Returns
    ----------
    ent : float
          :math: '-\sum_i p_i*\log_b p_i'
    
    Notes
    ----------
    If any of entry in the input is negative it throws an error.
    """
    
    if any(p<0.):
        raise ValueError('In entropy not all arguments positive')
    
    x = p[p>0.]
    
    ent = np.dot(x, np.log(x))/np.log(base)
    return -1*ent


# In[3]:

def probVec1(eps, x):
    r"""Returns a probability vector of length two which
    has an eps-log-singularity of the input rate
    
    Parameters
    ----------
    eps : float
          Should be between 0 and 1
          
    x : float
        Should be between 0 and 1
    
    Returns
    ----------
    prb : 1-d numpy array
          Length three, all positive entries sum to unity
          
    Notes
    ----------
    prb has the form (1-x*e, x*e)
    """
    return np.array([1-eps*x, eps*x])


# In[4]:

def probVec1D(eps, x,base=2.):
    r"""Returns the derivative of probability vector returned by
    probVec1D
    
    Parameters
    ----------
    eps : float
          Should be between 0 and 1
          
    x : float
        Should be between 0 and 1
     
    base : float
           Base for the log
           
    Returns
    ----------
    prb : 1-d numpy array
          Length three, all positive entries sum to unity
          
    Notes
    ----------
    prbD is -x*np.log(x * ep/ (1-x*ep))
    """
    der = np.log(ep) + np.log(x/(1-x*ep))
    der = -x*der/np.log(base)
    return der


# In[5]:

def probVec2(eps, x):
    r"""Returns a probability vector of length four which
    has an eps-log-singularity of the input rate
    
    Parameters
    ----------
    eps : float
          Should be between 0 and 1
          
    x : float
        Should be between 0 and 1
    
    Returns
    ----------
    prb : 1-d numpy array
          Length three, all positive entries sum to unity
          
    Notes
    ----------
    prb has the form (1-x*e, x*e/3, x*e/3, x*e/3)
    """
    return np.array([1-eps*x, eps*x/3, eps*x/3, eps*x/3])


# In[6]:

def probVec2D(eps, x,base=2.):
    r"""Returns the derivative of probability vector returned by
    probVec2D
    
    Parameters
    ----------
    eps : float
          Should be between 0 and 1
          
    x : float
        Should be between 0 and 1
     
    base : float
           Base for the log
           
    Returns
    ----------
    prb : 1-d numpy array
          Length three, all positive entries sum to unity
          
    Notes
    ----------
    prbD is -x*np.log(x * ep/ 3(1-x*ep))
    """
    der = np.log(ep) + np.log(x/(3-3*x*ep))
    der = -x*der/np.log(base)
    return der

