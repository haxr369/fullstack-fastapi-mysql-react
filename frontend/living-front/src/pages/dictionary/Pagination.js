import React,{useState, useEffect} from "react";
import './css/Pagination.css'
const Pagination = ({ currentPage, totalPages, onPageChange }) => {
  //let totalPlants =0;
  const pageNumbers = [];
  let showPages = 0;
  //let showPages =0;

  console.log("전체 페이지 수는? "+totalPages);
  for (let i = 1; i <= totalPages; i++) {
    pageNumbers.push(i);
  }
  
  
  return (
    <div className="pagination">
      {currentPage > 1 && (
        <button className="pagination__button" onClick={() => onPageChange(currentPage - 1)}>
          Prev
        </button>
      )}
      {pageNumbers.map((pageNumber) => (
        <button
          key={pageNumber}
          className={`pagination__button ${currentPage === pageNumber ? "active" : ""}`}
          onClick={() => onPageChange(pageNumber)}
        >
          {pageNumber}
        </button>
      ))}
      {currentPage < totalPages && (
        <button className="pagination__button" onClick={() => onPageChange(currentPage + 1)}>
          Next
        </button>
      )}
    </div>
  );
};

export default Pagination;