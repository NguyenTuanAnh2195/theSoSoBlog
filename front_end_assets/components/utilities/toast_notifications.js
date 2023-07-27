import { toast } from "react-toastify";

export const errorToast = (message = "An error occured!") => {
  return toast.error(message, {
    position: "top-center",
    autoClose: 15000,
    hideProgressBar: false,
    closeOnClick: true,
    pauseOnHover: true,
    draggable: true,
    progress: undefined,
    theme: "light",
  });
};

export const successToast = (message = "Operation successful!") => {
  return toast.success(message, {
    position: "top-center",
    autoClose: 15000,
    hideProgressBar: false,
    closeOnClick: true,
    pauseOnHover: true,
    draggable: true,
    progress: undefined,
    theme: "light",
  });
};
