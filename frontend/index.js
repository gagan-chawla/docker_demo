createUser = async (username, password) => {
  const params = {
    username: username,
    password: password,
  };
  console.log(params);
  response = await fetch("http://localhost:5001/", {
    method: "POST",
    body: JSON.stringify(params),
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  });
  console.log(await response.json());
};
