import torch

# Gradients are essential for model optimization

x = torch.randn(3, requires_grad=True)
print(x)