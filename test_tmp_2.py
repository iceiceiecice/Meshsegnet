from vedo import *
from visdom import Visdom

viz = Visdom()
viz.line([0.], [0.], win='train_loss',opts=dict(title='train loss', legend = ['train', 'val']))
viz.line([[0.0, 0.0]], [0.], win='test', opts=dict(title='test loss&acc.',
                                                   legend=['loss', 'acc.']))
# global_step = 0

# viz.line([loss.item()], [global_step], win='train_loss', update='append')


n = 10
epoch = 0
for i in range(n):
    viz.line([epoch], [0.5*i + 1], win = 'train_loss', update='append')
    viz.line([epoch], [i], win='train_loss', update='append', legend = 'val')
    # viz.line('SEN', 'train', 'asSEN', epoch, i)
    # viz.line('PPV', 'train', 'asPPV', epoch, i + 1)
    # viz.line('Loss', 'val', 'class Loss', epoch, 0.5*i + 2)
    # plotter.plot('DSC', 'val', 'DSC', i, 0.5*i + 2)
    # plotter.plot('SEN', 'val', 'SEN', i, i + 2)
    # plotter.plot('PPV', 'val', 'PPV', i, i + 3)
    epoch += 1