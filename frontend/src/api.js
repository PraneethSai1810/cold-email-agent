import axios from "axios";

const API = axios.create({
  baseURL: "https://cold-email-agent-q7l2.onrender.com",
});

export default API;