from vector import Vector3D

'''
              |- 1; W̅.x̄ >=0
ŷ = hᵥᵥ(x) =  |
              |- 0; otherwise

W̅.x̄ = ΣwᵢXᵢ {i=0, x=bias}

Preceptron Rule: 
wᵢ <- wᵢ + η(Δy)xᵢ
Δy = y - ŷ (difference of actual value and assumed value)
'''
weights = Vector3D(0,0,0)     # initial weights
l_rate = 0.1   # η


     