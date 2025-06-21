function openAddModal() {
  document.getElementById("studentForm").action = "/add/";
  document.getElementById("studentId").value = "";
  document.getElementById("studentName").value = "";
  document.getElementById("studentSubject").value = "";
  document.getElementById("studentMarks").value = "";
  document.getElementById("studentModal").style.display = "block";
}

function openEditModal(id, name, subject, marks) {
  document.getElementById("studentForm").action = "/edit/" + id + "/";
  document.getElementById("studentId").value = id;
  document.getElementById("studentName").value = name;
  document.getElementById("studentSubject").value = subject;
  document.getElementById("studentMarks").value = marks;
  document.getElementById("studentModal").style.display = "block";
}

function closeModal() {
  document.getElementById("studentModal").style.display = "none";
}

let deleteUrl = "";
function confirmDelete(url) {
  deleteUrl = url;
  document.getElementById("deleteModal").style.display = "block";
}

function proceedDelete() {
  window.location.href = deleteUrl;
}

function closeDeleteModal() {
  document.getElementById("deleteModal").style.display = "none";
}

function filterTable() {
  const input = document.getElementById("searchInput");
  const filter = input.value.toLowerCase();
  const rows = document.querySelectorAll("#studentTable tbody tr");

  rows.forEach((row) => {
    const name = row.children[0].textContent.toLowerCase();
    const subject = row.children[1].textContent.toLowerCase();
    row.style.display =
      name.includes(filter) || subject.includes(filter) ? "" : "none";
  });
}
