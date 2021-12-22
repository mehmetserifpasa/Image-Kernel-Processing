# Image-Kernel-Processing
Image Kernel, bizim bazı efektleri (keskinleştirme, bulanıklaştırma vb.) uygulamak için kullandığımız bir matrisi temsil eder.
Resimde aldığımız bir matris alanını parametrede verdiğimiz array ile işleme sokarak yeni bir pixel değeri elde etmemizi sağlıyor. Bu sayede
verdiğimiz array değerine göre yeni pixel değerleri üretiyor ve efekt uygulanmış oluyor. Aşşağıdaki görsele bakarak daha iyi anlayabilirsiniz:
![movie1-1-5](https://user-images.githubusercontent.com/25556230/147119721-340d15c4-37e8-4efd-9cbd-65098c529522.gif)




## Code
ImageKernel adındaki Class'ına verdiğimiz ilk parametre bizim efekt uygulamak istediğimiz resim. İkinci parametre ise bizim matris aralığımız. Örnek olarak 3x3
uygulanacağı için 3 verilmiştir. [[1, 2, 1], [0, 0, 0], [-1, -2, -1]] değeri ise bizim array aralığımız. Bu array listesine ulaşmak için kodun altına bunun ile ilgili
resim yüklüyorum. Bu değerleri değiştirerek resim üzerinde nasıl bir değişiklik olduğunu görebilirsiniz.
```
object = ImageKernel(
    "image.jpg",
    3,
    [[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
```
Array örnekleri:
![Typesofkernels](https://user-images.githubusercontent.com/25556230/147120485-5b794793-16db-40c3-b514-278e048f35c6.png)
Mesela Sharpen Kernel array'i resim üzerinde keskinleştirme yapmak için oluşturulmuş değerlerdir.




## Example 1
Bu örnekte "sobel operator" denilen bir array değeri kullanılmıştır. Bu array, resim üzerinde kenarları algılamak için kullanılan bir algoritmadır.
![Ekran Resmi 2021-12-22 19 07 25](https://user-images.githubusercontent.com/25556230/147121565-6cb790d3-2131-4a06-b2a1-340c61dcb44d.png)

## Example 2
Bu örnekte ise "emboss" denilen kabartma algoritması kullanılmıştır.
![Ekran Resmi 2021-12-22 19 10 22](https://user-images.githubusercontent.com/25556230/147121961-b26598e7-0328-4238-a515-4a26c7d13478.png)


## Kaynaklar
* https://setosa.io/ev/image-kernels/
* https://theailearner.com/tag/cv2-filter2d/
* https://www.geeksforgeeks.org/python-opencv-filter2d-function/
* https://learnopencv.com/image-filtering-using-convolution-in-opencv/
* https://datahacker.rs/004-how-to-smooth-and-sharpen-an-image-in-opencv/
* https://www.codingame.com/playgrounds/2524/basic-image-manipulation/filtering
