using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;
using System.Xml;
using System.Xml.Linq;

namespace EkranIothook
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        private async void button1_Click(object sender, EventArgs e)
        {
            try
            {
                string apiKey = "1c1094835fe305ad04096223";
                string startDate = textBox1.Text; // Başlangıç tarihi
                string endDate = textBox2.Text; // Bitiş tarihi

                // API isteği için URL oluştur
                string apiUrl = $"https://iothook.com/api/device/?api_key={apiKey}&start_date={startDate}&end_date={endDate}";

                using (HttpClient httpClient = new HttpClient())
                {
                    HttpResponseMessage response = await httpClient.GetAsync(apiUrl);

                    if (response.IsSuccessStatusCode)
                    {
                        string responseData = await response.Content.ReadAsStringAsync();

                        // Verileri görselleştirme işlemi için ayrı bir metodu çağır
                        ProcessResponseData(responseData);
                    }
                    else
                    {
                        MessageBox.Show("HTTP Error: " + response.StatusCode);
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }

        }

        // HttpResponse verisini işlemek için ayrı bir metot
        private async void ProcessResponseData(string responseData)
        {
            HttpClient httpClient = new HttpClient();

            // HttpRequestMessage oluşturulması
            HttpRequestMessage request = new HttpRequestMessage(HttpMethod.Get, "https://iothook.com/api/device/?api_key=1c1094835fe305ad04096223&results=1");
            request.Headers.Add("api_key", "1c1094835fe305ad04096223");

            HttpResponseMessage response = await httpClient.SendAsync(request);

            var responseString = await response.Content.ReadAsStringAsync();
            var statusCode = response.StatusCode;

            responseString = responseString.Replace("[", "").Replace("]", "");

            IothookMember member = JsonConvert.DeserializeObject<IothookMember>(responseString);
            string field_4 = member.field_4;
            string field_5 = member.field_5;
            string field_6 = member.field_6;

            double total = Convert.ToDouble(field_4) + Convert.ToDouble(field_5) + Convert.ToDouble(field_6);

            int percentageField4 = (int)((Convert.ToDouble(field_4) / total) * 100);
            int percentageField5 = (int)((Convert.ToDouble(field_5) / total) * 100);
            int percentageField6 = (int)((Convert.ToDouble(field_6) / total) * 100);

            chart2.Series["Yanma Sayısı"].Points.Add(new DataPoint(0, Convert.ToDouble(field_4)) { AxisLabel = $"Kırmızı (%{percentageField4})" });
            chart2.Series["Yanma Sayısı"].Points.Add(new DataPoint(0, Convert.ToDouble(field_5)) { AxisLabel = $"Yeşil (%{percentageField5})" });
            chart2.Series["Yanma Sayısı"].Points.Add(new DataPoint(0, Convert.ToDouble(field_6)) { AxisLabel = $"Sarı (%{percentageField6})" });
        }


        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private async void Form2_Load(object sender, EventArgs e)
        {
           
            
        }

        public class IothookMember
        {
            public string field_4 { get; set; }
            public string field_5 { get; set; }
            public string field_6 { get; set; }
        }

        public class Program
        {
            public static async Task Main()
            {
                HttpClient httpClient = new HttpClient();

                // HttpRequestMessage oluşturulması
                HttpRequestMessage request = new HttpRequestMessage(HttpMethod.Get, "https://iothook.com/api/device/?api_key=1c1094835fe305ad04096223&results=2");
                request.Headers.Add("api_key", "1c1094835fe305ad04096223");

                HttpResponseMessage response = await httpClient.SendAsync(request);

                string responseString = await response.Content.ReadAsStringAsync();
                var statusCode = response.StatusCode;

            }
        }

        private void chart2_Click(object sender, EventArgs e)
        {

        }
    }
}