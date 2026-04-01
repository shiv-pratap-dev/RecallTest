#  run for 1 image
#  user uploads a photo
#  run ocr + image recog
#  res(ocr) = make embeddings of those , store it in  faiss vector store 
#  run imge recog, object detection using yolo
#  store in faiss
#  use an embedder 
#  imp; have an image id, dono ki ek image , dono stored under one folder
stored_image{
    "imageid" : "uuid", # MUST
    "text_emd" : [[whdhdshc]], # ocr
    "image_emd" : [[whdhdshc]], # faiss
    "object details": 'deatils' = {
        'color';
        size,
        eyes color
        text available: ['all text retrived']
    }
}
#  lets start 
#  take original image using image id and store it in cloudfare contain :
image = {
    image url,
    image_id;
    basic_details;

}


#  connect these two 