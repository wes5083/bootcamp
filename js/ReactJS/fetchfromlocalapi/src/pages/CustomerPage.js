import React, { useState, useEffect } from "react";

const CustomerPage = () => {
  const [customerList, setCustomerList] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        fetch("http://localhost:5062/api/GetCustomers")
          .then((response) => response.json())
          .then((data) => {
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
      <table>
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
                <tr key={customer.customerID}>
                  <td>{customer.customerID}</td>
                  <td>{customer.companyName}</td>
                  <td>{customer.contactName}</td>
                  <td>{customer.contactTitle}</td>
                  <td>{customer.address}</td>
                  <td>{customer.city}</td>
                  <td>{customer.region}</td>
                  <td>{customer.postalCode}</td>
                  <td>{customer.country}</td>
                  <td>{customer.phone}</td>
                  <td>{customer.fax}</td>
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
