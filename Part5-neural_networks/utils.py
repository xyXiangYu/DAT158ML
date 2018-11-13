import numpy as np
import matplotlib.pyplot as plt
import torch
import torchvision
from torchvision import transforms

classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')


def get_cifar10(batch_size=4):

    transform = transforms.Compose(
        [transforms.ToTensor(), transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))])

    trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
    testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size,  shuffle=True, num_workers=2)
    testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size, shuffle=False, num_workers=2)

    return trainloader, testloader


trainloader, testloader = get_cifar10(batch_size=4)

def plot_cifar10():
        images, labels = iter(trainloader).next()
        img = torchvision.utils.make_grid(images)
        img = img.numpy()/2 + 0.5
        img = np.transpose(img, (1, 2, 0))
        
        f = plt.figure(figsize=(10,6))
        plt.axis("Off")
        plt.imshow(img)
        plt.show()
        print(f'{[classes[labels[j]] for j in range(4)]}')