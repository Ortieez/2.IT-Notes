---

creation date: <% tp.file.creation_date() %>

modification date: <% tp.file.last_modified_date("dddd Do MMMM YYYY HH:mm:ss") %>

---

<< [[<% tp.date.now("YYYY-MM-DD", -1) %>]] | [[<% tp.date.now("YYYY-MM-DD", 1) %>]] >>

# <% tp.file.title %>

### What is on your mind?

---

<%* if (tp.date.now("M-D") == 1-1) { %>
[ ] Make Yearly Note
<%* } %>

<% tp.web.daily_quote() %>