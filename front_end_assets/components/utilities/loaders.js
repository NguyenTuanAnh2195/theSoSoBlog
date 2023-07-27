import {
  getBlogPostById
} from "./api_calls";

export async function blogByIdLoader({ params }) {
  return getBlogPostById(params.blogId);
}
