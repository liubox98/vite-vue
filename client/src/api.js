import axios from "axios";

const api = axios.create({
  baseURL: "/api",
});

export const fetchData = () => {
  return api.get("/data");
};

export const postDate = (data) => {
  return api.post("/post", data);
};
