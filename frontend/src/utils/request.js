async function CreateUser() {
    fetch("http://localhost:8000/create_user", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        unique_nickname: "andrey_dev",
        email: "andreypremiere@mail.ru",
        number_phone: "+79998887766"
    })
    })
    .then(response => {
        if (!response.ok) {
        throw new Error("Ошибка при создании пользователя");
        }
        return response.json();
    })
    .then(data => {
        console.log("Ответ сервера:", data);
        /*
        {
            user_id: "b3cf4de5-...-8d38",
            unique_nickname: "andrey_dev",
            email: "andrey@example.com",
            number_phone: "+79998887766",
            displayed_nickname: "Андрей"
        }
        */
    })
    .catch(error => {
        console.error("Ошибка:", error);
  });
}