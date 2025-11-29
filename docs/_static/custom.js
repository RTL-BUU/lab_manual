document.addEventListener("DOMContentLoaded", function() {
    // หาลิงก์ทั้งหมดที่เป็นลิงก์ภายนอก (External Link)
    var links = document.querySelectorAll("a.reference.external");
    
    // วนลูปสั่งให้เปิด Tab ใหม่ทุกอัน
    for (var i = 0; i < links.length; i++) {
        links[i].setAttribute("target", "_blank");
        links[i].setAttribute("rel", "noopener noreferrer");
    }
});