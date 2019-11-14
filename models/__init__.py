# from .vavanilla_resnet_cifar import vanilla_resnet20
from .vanilla_models.vanilla_resnet_imagenet import resnet18


from .quan_resnet_imagenet import resnet18_quan, resnet34_quan

from .quan_alexnet_imagenet import alexnet_quan

from .quan_mobilenet_imagenet import mobilenet_v2_quan
from .vanilla_models.vanilla_mobilenet_imagenet import mobilenet_v2



############## ResNet for CIFAR-10 ###########
from .vanilla_models.vanilla_resnet_cifar import vanilla_resnet20
from .quan_resnet_cifar import resnet20_quan

############## VGG for CIFAR #############

from .vanilla_models.vanilla_vgg_cifar import vgg11_bn, vgg11
from .quan_vgg_cifar import vgg11_bn_quan, vgg11_quan

from .test_model import vgg_test