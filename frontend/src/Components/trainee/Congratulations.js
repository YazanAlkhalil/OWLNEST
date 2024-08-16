import { TextField } from "@mui/material";
import React, { useState } from "react";
import ReactStars from "react-stars";
import useFetch from "../AuthComponents/UseFetch";
import { useParams } from "react-router-dom";

const Congratulations = ({ courseName, certificateUrl, onSubmitReview }) => {
  const [description, setDescription] = useState("");
  const [rate, setRating] = useState(0);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmitReview({ description, rate });
  };

  return (
    <div className="max-w-2xl mx-auto mt-10 p-6  rounded-lg shadow-xl">
      <h1 className="text-3xl font-bold text-center text-green-600 mb-6">
        Congratulations!
      </h1>
      <p className="text-xl text-center mb-6">
        You've successfully completed the course:
        <span className="font-semibold block mt-2">{courseName}</span>
      </p>

      <div className="mb-6">
        <h2 className="text-2xl font-semibold mb-3">Your Certificate</h2>
        <img
          src={certificateUrl}
          alt="Course Certificate"
          className="w-full h-[400px] border-2 border-gray-300 rounded-lg"
        />
      </div>

      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label htmlFor="review" className="block text-lg font-medium mb-2">
            Leave a Review
          </label>
          <TextField id="outlined-basic"
          onChange={(e) => setDescription(e.target.value)}
          label="Review" variant="outlined" />
        </div>

        <div>
          <label className="block text-lg font-medium mb-2">
            Rate the Course
          </label>
          <ReactStars
            count={5}
            onChange={setRating}
            size={24}
            color2={"#ffd700"}
            half={false}
          />
        </div>

        <button
          type="submit"
          className="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition duration-300">
          Submit Review
        </button>
      </form>
    </div>
  );
};

function CourseCompletion() {
  const { fetchData, resData } = useFetch();
  const {id} = useParams();
  const companyId = localStorage.getItem('companyId')

  const handleReviewSubmit = async (reviewData) => {
    console.log(reviewData);
    const res = await fetchData({url:`http://127.0.0.1:8000/api/trainee/company/${companyId}/courses/${id}/review`,
      method:"POST",
      data: reviewData
    })
    console.log(res);
    
   
  };

  return (
    <Congratulations
      courseName="Introduction to React"
      certificateUrl="https://cdn4.vectorstock.com/i/1000x1000/79/33/certification-icon-symbol-creative-sign-from-gdpr-vector-27647933.jpg"
      onSubmitReview={handleReviewSubmit}
    />
  );
}

export default CourseCompletion;
