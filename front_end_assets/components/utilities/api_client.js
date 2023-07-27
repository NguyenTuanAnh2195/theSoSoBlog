import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:8003/api/v1',
  timeout: 3000,
});

const navigate = useNavigate();

apiClient.interceptors.request.use((config) => {
  if (!localStorage.getItem("tokens")) {
    navigate("/login");
  }
  const token = JSON.parse(localStorage.getItem("tokens"));
  config.headers.common["Authorization"] = `Bearer ${token.access_token}`;
  return config;
});

apiClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response.status === 401) {
      const tokens = JSON.parse(localStorage.getItem("tokens"));
      const payload = {
        refresh: tokens.refreshToken,
      };

      const response = await axios.post(
        `${apiClient.baseURL}/auth/token/refresh`,
        payload
      );
      localStorage.setItem("tokens", JSON.stringify(response.data));
      error.config.headers["Authorization"] = `Bearer ${response.data.access_token}`
    } else {
      return Promise.reject(error);
    }
  }
);

export default apiClient;
