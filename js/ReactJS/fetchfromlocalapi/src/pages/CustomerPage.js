import React, { useState, useEffect } from "react";

const CustomerPage = () => {
  const [customerList, setCustomerList] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        fetch("http://localhost:5000/api/customers")
          .then((response) => response.json())
          .then((data) => {
            console.log(data);
            setCustomerList(data);
          });
        setIsLoading(false);
      } catch (error) {
        console.log(error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <table border="1">
        <thead>
          <tr>
            <th>ID</th>
            <th>Company Name</th>
            <th>Contact Name</th>
            <th>Contact Title</th>
            <th>Address</th>
            <th>City</th>
            <th>Region</th>
            <th>Postal Code</th>
            <th>Country</th>
            <th>Phone</th>
            <th>Fax</th>
          </tr>
        </thead>
        <tbody>
          {isLoading ? (
            <tr>
              <td>Data isLoading......</td>
            </tr>
          ) : (
            customerList &&
            customerList.map((customer) => {
              return (
                <tr key={customer.CustomerID}>
                  <td>{customer.CustomerID}</td>
                  <td>{customer.CompanyName}</td>
                  <td>{customer.ContactName}</td>
                  <td>{customer.ContactTitle}</td>
                  <td>{customer.Address}</td>
                  <td>{customer.City}</td>
                  <td>{customer.Region}</td>
                  <td>{customer.PostalCode}</td>
                  <td>{customer.Country}</td>
                  <td>{customer.Phone}</td>
                  <td>{customer.Fax}</td>
                </tr>
              );
            })
          )}
        </tbody>
      </table>
    </div>
  );
};

export default CustomerPage;
