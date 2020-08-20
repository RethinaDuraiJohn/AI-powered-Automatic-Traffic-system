var img = new Image();
img.src = "https://image.shutterstock.com/image-photo/mountains-during-sunset-beautiful-natural-260nw-407021107.jpg"
ctx.drawImage(img, 0, 0);
var imgData = ctx.getImageData(x, y, width, height).data;
console.log(imgData)