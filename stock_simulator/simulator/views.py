from rest_framework.decorators import api_view
from rest_framework.response import Response
import numpy as np

def geometric_brownian_motion(S0, mu, sigma, T, dt):
    n = round(T/dt)
    t = np.linspace(0, T, n)
    W = np.random.standard_normal(size = n)
    W = np.cumsum(W)*np.sqrt(dt) ### standard brownian motion ###
    X = (mu-0.5*sigma**2)*t + sigma*W 
    S = S0*np.exp(X) ### geometric brownian motion ###
    return S.tolist()

# Provides a single API endpoint /simulate 
@api_view(['POST'])
def simulate(request):
    S0 = request.data.get('S0', 100)
    mu = request.data.get('mu', 0.05)
    sigma = request.data.get('sigma', 0.2)
    T = request.data.get('T', 1)  # Total time in years
    dt = request.data.get('dt', 0.01)  # Time step in years
    simulations = request.data.get('simulations', 100)
    results = [geometric_brownian_motion(S0, mu, sigma, T, dt) for _ in range(simulations)]
    return Response({'paths': results})