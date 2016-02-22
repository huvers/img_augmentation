# img_augmentation
<h2>
Python scripts for creating synthetic image data for Machine Learning
</h2>


create_synthetic_imgs.py usage:
```
    python create_synthetic_data.py [folder]
```


Will operate on a folder containing either images or subfolders with images, and create a combinatorial mix of rotations, contrast changes, color changes, and randomly added gaussian noise. Current settings will create ~ 950 synthetic images for each image given. Reduce the # of noise images from 200 to whatever you desire for fewer synthetic copies.

<h3>
Example
</h3>
<h4>
Original Image
</h4>
![Alt desc](https://github.com/huvers/img_augmentation/blob/master/orig_98.png)
<h4>
Synthetic Image
</h4>
![Alt desc](https://github.com/huvers/img_augmentation/blob/master/synthetic_98.png)
