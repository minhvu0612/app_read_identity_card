# app_read_identity_card
  +, ứng dụng đọc thông tin chứng minh nhân dân của người dùng

# use case diagram

  +, user cho ảnh/thẻ chứng minh nhân nhân/căn cước công dân vào camera để quét.
  
  +, sau khi quét camera sẽ gửi dữ liệu ảnh đã đọc được đến ứng dụng, sau khi xử lý ứng dụng sẽ trích xuất các thông tin về user và gửi về hệ thống.
  
  +, hệ thống có nhiệm vụ lưu trữ thông tin về người dùng và tra về thông tin của người dùng đó khi truy vấn.
  
  +, admin có thể truy xuất vào thông tin về dữ liệu của user.


# tech using

  +, Frontend:  ReactJS
  
  +, Backend:   Django, Python
  
  +, Algorithm: KNN, Flood-Fill, CNN
