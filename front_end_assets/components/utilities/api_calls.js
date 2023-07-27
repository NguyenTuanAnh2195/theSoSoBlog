import apiClient from "./api_client";
import { errorToast } from "./toast_notifications";

export function getBlogPostById(id) {
  response = apiClient.get(`/blog/${id}`)
    .then(function (response){
      return JSON.parse(response)
    })
    .catch(function (error) {
      errorToast();
    })
};
