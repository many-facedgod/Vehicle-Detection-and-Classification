f=fopen('list.txt','r');
for i=1:1538
    s=fgetl(f);
    img=imread(s);
    se=strel('square',5);
    nimg=imerode(img,se);
    nimg=imerode(img,se);
    nimg=imdilate(nimg,se);
    nimg=imerode(nimg,se);
    nimg=imdilate(nimg,se);
    name=strcat('image',num2str(i),'.jpg');
    imwrite(nimg,name);
end